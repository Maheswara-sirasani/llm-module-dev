from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId
from database import db
from auth import get_current_user, require_admin
from pydantic import BaseModel
from typing import Optional, List
 
router = APIRouter(prefix="/vehicles", tags=["vehicles"])
 
class VehicleCreate(BaseModel):
    type: str
    model: str
    plate_number: str
    price_per_hour: float
    available: Optional[bool] = True
 
class VehicleOut(BaseModel):
    id: str
    type: str
    model: str
    plate_number: str
    price_per_hour: float
    available: bool
 
@router.post("/", response_model=VehicleOut, status_code=status.HTTP_201_CREATED)
async def add_vehicle(vehicle: VehicleCreate, admin=Depends(require_admin)):
    doc = vehicle.dict()
    res = await db.vehicles.insert_one(doc)
    created = await db.vehicles.find_one({"_id": res.inserted_id})
    return VehicleOut(
        id=str(created["_id"]),
        type=created["type"],
        model=created["model"],
        plate_number=created["plate_number"],
        price_per_hour=created["price_per_hour"],
        available=created["available"]
    )
    
@router.put("/{vehicle_id}", response_model=VehicleOut)
async def update_vehicle(vehicle_id: str, vehicle: VehicleCreate, admin=Depends(require_admin)):
    update_data = {k: v for k, v in vehicle.dict().items() if v is not None}
    result = await db.vehicles.update_one({"_id": ObjectId(vehicle_id)}, {"$set": update_data})
 
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Vehicle not found")
 
    updated = await db.vehicles.find_one({"_id": ObjectId(vehicle_id)})
    return VehicleOut(
        id=str(updated["_id"]),
        type=updated["type"],
        model=updated["model"],
        plate_number=updated["plate_number"],
        price_per_hour=updated["price_per_hour"],
        available=updated["available"]
    )
 
@router.delete("/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicle(vehicle_id: str, admin=Depends(require_admin)):
    result = await db.vehicles.delete_one({"_id": ObjectId(vehicle_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return {"message": "Vehicle deleted successfully"}
 
@router.get("/", response_model=List[VehicleOut])
async def list_vehicles(current_user=Depends(get_current_user)):
    vehicles = await db.vehicles.find({"available": True}).to_list(100)
    return [
        VehicleOut(
            id=str(v["_id"]),
            type=v["type"],
            model=v["model"],
            plate_number=v["plate_number"],
            price_per_hour=v["price_per_hour"],
            available=v["available"]
        )
        for v in vehicles
    ]
 
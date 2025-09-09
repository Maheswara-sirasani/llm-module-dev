
from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId
from bson.errors import InvalidId
from datetime import datetime, timedelta
from typing import List
from pydantic import BaseModel
 
from database import db
from auth import get_current_user,require_admin
 
router = APIRouter(prefix="/bookings", tags=["bookings"])
 
 
class BookingCreate(BaseModel):
    vehicle_id: str
    hours: int
 
 
class BookingOut(BaseModel):
    id: str
    user_id: str
    vehicle_id: str
    start_time: datetime
    end_time: datetime
    total_price: float
 
 
@router.post("/", response_model=BookingOut, status_code=status.HTTP_201_CREATED)
async def book_vehicle(booking: BookingCreate, current_user=Depends(get_current_user)):
    try:
        vehicle_obj_id = ObjectId(booking.vehicle_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid vehicle id")
 
    vehicle = await db.vehicles.find_one({"_id": vehicle_obj_id})
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    if not vehicle.get("available", True):
        raise HTTPException(status_code=400, detail="Vehicle is not available")
 
    start_time = datetime.utcnow()
    end_time = start_time + timedelta(hours=booking.hours)
    total_price = booking.hours * vehicle["price_per_hour"]
    user_id_str = str(current_user.get("_id") or current_user.get("id"))
    try:
        user_obj_id = ObjectId(user_id_str)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user id in token")
 
    booking_doc = {
        "user_id": user_obj_id,
        "vehicle_id": vehicle_obj_id,
        "start_time": start_time,
        "end_time": end_time,
        "total_price": total_price,
    }
    res = await db.bookings.insert_one(booking_doc)
    await db.vehicles.update_one({"_id": vehicle_obj_id}, {"$set": {"available": False}})
 
    return BookingOut(
        id=str(res.inserted_id),
        user_id=str(user_obj_id),
        vehicle_id=str(vehicle_obj_id),
        start_time=start_time,
        end_time=end_time,
        total_price=total_price,
    )
 
 
@router.get("/my", response_model=List[BookingOut])
async def my_bookings(current_user=Depends(get_current_user)):
    user_id_str = str(current_user.get("_id") or current_user.get("id"))
    try:
        user_obj_id = ObjectId(user_id_str)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user id in token")
 
    bookings = await db.bookings.find({"user_id": user_obj_id}).to_list(100)
    return [
        BookingOut(
            id=str(b["_id"]),
            user_id=str(b["user_id"]),
            vehicle_id=str(b["vehicle_id"]),
            start_time=b["start_time"],
            end_time=b["end_time"],
            total_price=b["total_price"],
        )
        for b in bookings
    ]
 
class BookingWithVehicleOut(BaseModel):
    id: str
    user_id: str
    vehicle_id: str
    vehicle_model: str
    start_time: datetime
    end_time: datetime
    total_price: float
 
 
@router.get("/all", response_model=List[BookingWithVehicleOut])
async def all_bookings(admin=Depends(require_admin)):
    """
    Admin: View all bookings with vehicle details
    """
    pipeline = [
        {
            "$lookup": {
                "from": "vehicles",
                "localField": "vehicle_id",
                "foreignField": "_id",
                "as": "vehicle"
            }
        },
        {"$unwind": "$vehicle"},
    ]
 
    bookings = await db.bookings.aggregate(pipeline).to_list(100)
 
    return [
        BookingWithVehicleOut(
            id=str(b["_id"]),
            user_id=str(b["user_id"]),
            vehicle_id=str(b["vehicle_id"]),
            vehicle_model=b["vehicle"]["model"],
            start_time=b["start_time"],
            end_time=b["end_time"],
            total_price=b["total_price"],
        )
        for b in bookings
    ]
  
from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, schemas, database, vpn_manager

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="VPN Admin Panel")

app.mount("/configs", StaticFiles(directory="wg_configs"), name="configs")

@app.post("/api/users/", response_model=schemas.VPNUserOut)
def create_user(user: schemas.VPNUserCreate, db: Session = Depends(database.get_db)):
    existing = db.query(models.VPNUser).filter(models.VPNUser.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    vpn_data = vpn_manager.create_vpn_user(user.username)
    db_user = models.VPNUser(**vpn_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/api/users/", response_model=list[schemas.VPNUserOut])
def list_users(db: Session = Depends(database.get_db)):
    return db.query(models.VPNUser).all()

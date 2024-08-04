from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    uploads = relationship("Upload", back_populates="owner")

class Upload(Base):
    __tablename__ = "uploads"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    file_size = Column(Integer)
    status = Column(String)
    encrypted_key = Column(String)
    upload_time = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="uploads")
    validation_result = relationship("ValidationResult", back_populates="upload", uselist=False)

class ValidationResult(Base):
    __tablename__ = "validation_results"

    id = Column(Integer, primary_key=True, index=True)
    upload_id = Column(Integer, ForeignKey("uploads.id"))
    file_a_status = Column(String)
    file_b_status = Column(String)
    file_c_status = Column(String)
    validation_time = Column(DateTime(timezone=True), server_default=func.now())

    upload = relationship("Upload", back_populates="validation_result")
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, JSON
from sqlalchemy.orm import relationship

from app.db.session import Base


class ExchangeCredentials(Base):
    __tablename__ = "exchange_credentials"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    exchange_name = Column(String, nullable=False)
    # Common field for all exchanges
    api_key = Column(String, nullable=True)  # Made nullable for exchanges like DEX that might not need it
    # Store additional auth params as JSON to handle different exchange requirements
    auth_params = Column(JSON, nullable=True)  # Stores api_secret, passphrase, etc.
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    
    # Relationship to user
    user = relationship("User", back_populates="exchange_credentials")
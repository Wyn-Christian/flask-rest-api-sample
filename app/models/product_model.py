# app/models/product_model.py

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import  ForeignKey

from app.extensions import db


class Product(db.Model):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    price: Mapped[float]
    stock: Mapped[int] = mapped_column(default=0)

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("user_account.id"),
    )
    owner: Mapped["User"] = relationship(back_populates="products")

    def __repr__(self):
        return f"<Product {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
        }

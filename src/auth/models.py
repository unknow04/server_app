from datetime import datetime

from sqlalchemy import MetaData, Table, TIMESTAMP, Column, Integer, String, BOOLEAN, ForeignKey, JSON

metadata_auth = MetaData()

roles = Table(
    "roles",
    metadata_auth,
    Column("id", Integer, primary_key=True),
    Column("role_name", String, nullable=False),
    Column("permissions", JSON)

)

users = Table(
    "users",
    metadata_auth,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_name", String(30), nullable=False),
    Column("age", Integer, default=0),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("role_id", ForeignKey("roles.id"), nullable=False),
    Column("is_root", BOOLEAN, default=False),
    Column("reg_data", TIMESTAMP, default=datetime.utcnow)
)

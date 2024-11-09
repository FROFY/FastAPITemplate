from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.dao.database import Base, str_uniq


class Role(Base):
    name: Mapped[str_uniq]
    users: Mapped[list["User"]] = relationship(back_populates="role", foreign_keys="User.role_id")
    user_role: Mapped["User"] = relationship(back_populates="old_role", foreign_keys="User.role_id_old")

    def __repr__(self):
        return f"{self.__class__.__name__}(row_id={self.row_id}, name={self.name})"


class User(Base):
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str_uniq]
    password: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.row_id'), default=1, server_default=text("1"))
    role_id_old: Mapped[int] = mapped_column(ForeignKey('roles.row_id'), default=1, server_default=text("1"))
    role: Mapped["Role"] = relationship("Role",
                                        back_populates="users",
                                        lazy="joined",
                                        foreign_keys=[role_id])
    old_role: Mapped["Role"] = relationship("Role",
                                            back_populates="user_role",
                                            lazy="joined",
                                            uselist=False,
                                            foreign_keys=[role_id_old])
    # lazy="joined" сразу делает джоин при селекте этой таблицы

    def __repr__(self):
        return f"{self.__class__.__name__}(row_id={self.row_id})"

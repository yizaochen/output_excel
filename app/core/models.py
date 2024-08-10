from sqlalchemy import INTEGER, TEXT
from sqlalchemy.orm import mapped_column, Mapped
from core.database import Base
from datetime import date


# AR transaction record
class CTBCForeignBankSlip(Base):
    __tablename__ = "AutoAR_CTBCForeign_BankSlip"

    id: Mapped[int] = mapped_column("id", INTEGER, primary_key=True)
    BankSlipDate: Mapped[date] = mapped_column("BankSlipDate", TEXT, nullable=False)
    CustomerID: Mapped[str] = mapped_column("CustomerID", TEXT, nullable=False)
    BankCode: Mapped[str] = mapped_column("BankCode", TEXT, nullable=False)
    BankSlipCurrency: Mapped[str] = mapped_column(
        "BankSlipCurrency", TEXT, nullable=False
    )
    BankSlipAmount: Mapped[str] = mapped_column("BankSlipAmount", TEXT, nullable=False)
    CustomerName: Mapped[str] = mapped_column("CustomerName", TEXT, nullable=False)
    BankSlipCustomer: Mapped[str] = mapped_column(
        "BankSlipCustomer", TEXT, nullable=False
    )
    Country: Mapped[str] = mapped_column("Country", TEXT, nullable=False)
    FilePath: Mapped[str] = mapped_column("FilePath", TEXT, nullable=False)
    PredictType: Mapped[str] = mapped_column(
        "PredictType", TEXT, nullable=False
    )  # ('A', 'B', 'C', 'D')
    ProcessStatus: Mapped[str] = mapped_column(
        "ProcessStatus", TEXT, nullable=False
    )  # ('Processing', 'Fail', 'Finish', 'Cancel', 'Duplicate')
    ReferenceNumber: Mapped[str] = mapped_column(
        "ReferenceNumber", TEXT, nullable=False
    )
    RemitType: Mapped[str] = mapped_column("RemitType", TEXT, nullable=False)
    BankSlipRemark: Mapped[str] = mapped_column("BankSlipRemark", TEXT, nullable=False)
    ChangeDate: Mapped[date] = mapped_column("ChangeDate", TEXT, nullable=False)
    ArNo: Mapped[str] = mapped_column(
        "ArNo", TEXT, nullable=False
    )  # 入帳成功後寫入傳票號碼

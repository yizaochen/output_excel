from sqlalchemy import INTEGER, TEXT
from sqlalchemy.orm import mapped_column, Mapped
from core.database import Base
from datetime import date


# AR transaction record
class CTBCForeignBankSlip(Base):
    """
    PredictType: ('A', 'B', 'D', 'E', 'F'), D is the special customer. In frontend, A light, E medium, F dark

    """

    __tablename__ = "AutoAR_CTBCForeign_BankSlip"

    id: Mapped[int] = mapped_column("id", INTEGER, primary_key=True, autoincrement=True)
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
    )  # ('A', 'B', 'D', 'E', 'F')
    ProcessStatus: Mapped[str] = mapped_column(
        "ProcessStatus", TEXT, nullable=False
    )  # ('Wait-For-Check', 'Finish')
    ReferenceNumber: Mapped[str] = mapped_column(
        "ReferenceNumber", TEXT, nullable=False
    )
    RemitType: Mapped[str] = mapped_column("RemitType", TEXT, nullable=False)
    BankSlipRemark: Mapped[str] = mapped_column("BankSlipRemark", TEXT, nullable=False)
    ChangeDate: Mapped[date] = mapped_column("ChangeDate", TEXT, nullable=False)
    ArNo: Mapped[str] = mapped_column(
        "ArNo", TEXT, nullable=False
    )  # 入帳成功後寫入傳票號碼


# This is the mapping table for SAP customer-id and customer-name
class CTBCForeignSAP(Base):
    __tablename__ = "AutoAR_CTBCForeign_SAP_map"

    id = mapped_column("id", INTEGER, primary_key=True)
    CustomerID = mapped_column("CustomerID", TEXT, nullable=False)
    CustomerName = mapped_column("CustomerName", TEXT, nullable=False)


# D-type customer
class CTBCForeignSpecialCustomer(Base):

    __tablename__ = "AutoAR_CTBCForeign_SpecialCustomer"
    id = mapped_column("id", INTEGER, primary_key=True)
    CustomerName = mapped_column("CustomerName", TEXT, nullable=False)

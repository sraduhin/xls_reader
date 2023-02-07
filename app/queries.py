from app.models import Data
from app.utils import get_fields_name
from sqlalchemy import and_, text, sql
from db import db_session

def get_all():
    query = Data.query.order_by(Data.created_at).all()
    columns = get_fields_name(Data)
    print('{:^10} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^10}'.format(*columns[1:]))
    fmt = '{:10s} | {:11d} | {:11d} | {:11d} | {:11d} | {:12d} | {:12d} | {:12d} | {:12d} | {:10s}'
    for i in query:
        print(fmt.format(
            i.company,
            i.qliq_1_fact,
            i.qliq_2_fact,
            i.qoil_1_fact,
            i.qoil_2_fact,
            i.qliq_1_frcst,
            i.qliq_2_frcst,
            i.qoil_1_frcst,
            i.qoil_2_frcst,
            str(i.created_at),
        )
    )
    print('-' * 140)
    print(f'Total')


def get_total(start_date, end_date):
    result = db_session.query(
        Data.company, sql.func.sum(Data.qoil_2_frcst)
    ).group_by(Data.company).filter(Data.created_at >= start_date).filter(Data.created_at <= end_date).all()
    print(result)
    #rows = Data.query.filter(Data.created_at <= end_date).filter(Data.created_at >= start_date).all()


if __name__ == "__main__":
    get_total('2023-02-04', '2023-02-05')
    
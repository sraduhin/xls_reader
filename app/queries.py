from app.models import Data
from app.utils import get_fields_name
from sqlalchemy import and_, text, sql
from db import db_session

def get_all():
    query = Data.query.order_by(Data.created_at).all()
    columns = get_fields_name(Data)
    print('{:^10} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^10}'.format('', *columns[2:]))
    print('-' * 140)
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


def get_total(start_date, end_date):
    query = db_session.query(
        Data.company,
        sql.func.sum(Data.qliq_1_fact),
        sql.func.sum(Data.qliq_2_fact),
        sql.func.sum(Data.qoil_1_fact),
        sql.func.sum(Data.qoil_1_fact),
        sql.func.sum(Data.qliq_1_frcst),
        sql.func.sum(Data.qliq_2_frcst),
        sql.func.sum(Data.qoil_1_frcst),
        sql.func.sum(Data.qoil_2_frcst),
    ).group_by(Data.company).filter(Data.created_at >= start_date).filter(Data.created_at <= end_date).all()
    columns = get_fields_name(Data)
    columns = [f'total_{i}' for i in columns[2:-1]]
    print(query)
    print('{:^10} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9}'.format('', *columns))
    fmt = '{:10s} | {:16d} | {:16d} | {:16d} | {:16d} | {:17d} | {:17d} | {:17d} | {:17d}'
    for row in query:
        for i in row:
            print(fmt.format(*i))
    print('-' * 140)


if __name__ == "__main__":
    get_total('2023-02-04', '2023-02-05')
    
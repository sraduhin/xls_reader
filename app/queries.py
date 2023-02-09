from app.models import Data
from app.utils import get_fields_name
from sqlalchemy import and_, sql
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
    ).group_by(Data.company).filter(and_(Data.created_at >= start_date, Data.created_at <= end_date)).all()
    columns = get_fields_name(Data)
    columns = [f'total_{i}' for i in columns[2:-1]]
    print('{:^10} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9}'.format('', *columns))
    print('-' * 180)
    fmt = '{:10s} | {:17d} | {:17d} | {:17d} | {:17d} | {:18d} | {:18d} | {:18d} | {:18d}'
    for row in query:
        print(fmt.format(*row))
    print('-' * 180)


if __name__ == "__main__":
    get_total('2023-02-04', '2023-02-05')
    

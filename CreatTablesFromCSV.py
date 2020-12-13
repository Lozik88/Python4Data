
from sqlalchemy import create_engine
import config
import pandas as pd
import psycopg2
from tableschema import Table, infer, Schema
from functions.recursivejson import extract_values
from sqlalchemy.types import Integer, Text, Date


class CreateTablesFromCSVs:
    """Infer a table schema from a CSV."""

    __uri = config.PG_URI
    __engine = create_engine(__uri, convert_unicode=True, echo=True)
    __data =r'/home/lozik/CodeProjects/PyProjects/Python4Data/2m Sales Records.csv'

    @classmethod
    def get_data(cls):
        """Pull latest data."""
        test_df = pd.read_csv(cls.__data, header=0, encoding='utf-8')
        return test_df

    @classmethod
    def get_schema_from_csv(cls, csv):
        """Infers schema from CSV."""
        table = Table(csv)
        table.infer(limit=500, confidence=0.55)
        schema = table.schema.descriptor
        names = cls.get_column_names(schema, 'name')
        datatypes = cls.get_column_datatypes(schema, 'type')
        schema_dict = dict(zip(names, datatypes))
        return schema_dict

    @classmethod
    def get_column_names(cls, schema, key):
        """Get names of columns."""
        names = extract_values(schema, key)
        return names

    @classmethod
    def get_column_datatypes(cls, schema, key):
        """Convert schema to recognizable by SQLAlchemy."""
        values = extract_values(schema, key)
        for i, value in enumerate(values):
            if value == 'integer':
                values[i] = Integer
            elif value == 'string':
                values[i] = Text
            elif value == 'date':
                values[i] = Date
        return values

    @classmethod
    def create_new_table(cls, data, schema):
          """Create new table from CSV and generated schema."""
          workday_table.to_sql('faketable',
                               con=cls.__engine,
                               schema='testschema',
                               if_exists='replace',
                               chunksize=300,
                               dtype=schema)

data = CreateTablesFromCSVs.get_schema_from_csv()
schema = CreateTablesFromCSVs.get_schema_from_csv(data)
CreateTablesFromCSVs.create_new_table(data, schema)







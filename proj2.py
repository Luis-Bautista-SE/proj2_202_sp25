import sys
sys.setrecursionlimit(10_000)
import csv
import math
from dataclasses import dataclass
from typing import *

#Task 1
#The purpose of this task is to define the linked lists with classes with Row and Node.
# Put your data definitions first!
@dataclass(frozen=True)
class Row:
    country: str
    year: int
    electricity_and_heat_co2_emissions: Optional[float]
    electricity_and_heat_co2_emissions_per_capita: Optional[float]
    energy_co2_emissions: Optional[float]
    energy_co2_emissions_per_capita: Optional[float]
    total_co2_emissions_excluding_lucf: Optional[float]
    total_co2_emissions_excluding_lucf_per_capita: Optional[float]
@dataclass(frozen=True)
class Node:
    value: Row
    next: Node|None





#Task 2
#The purpose of this function is to read through the cvs file and return them as rows objects connected through a linked list
# Then your functions.
#Helper Funcs
def parse_row(fields: list[str]) -> Row:
    def to_float(value: str):
        if value != "":
            return float(value)
        return None
    return Row(
        country=fields[0],
        year=int(fields[1]),
        electricity_and_heat_co2_emissions=to_float(fields[2]),
        electricity_and_heat_co2_emissions_per_capita=to_float(fields[3]),
        energy_co2_emissions=to_float(fields[4]),
        energy_co2_emissions_per_capita=to_float(fields[5]),
        total_co2_emissions_excluding_lucf=to_float(fields[6]),
        total_co2_emissions_excluding_lucf_per_capita=to_float(fields[7]),)
def build_list(rows: list[Row]) -> Optional[Node]:
    if not rows:
        return None
    return Node(rows[0], build_list(rows[1:]))
#Actual Func
def read_csv_lines(filename: str) -> Optional[Node]:
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [parse_row(row) for row in reader]
        return build_list(rows)

#Task 3
#The purpose of this function is to return the number of rows in the linked list
def listlen(data: Optional[Node]) -> int:
    if data is None:
        return 0
    return 1 + listlen(data.next)
#Task 4
#The purpose of this function is to filter through the cvs files and make comparison between different rows on their values
#returning what the comparison is asking for.
def filter_rows(
    data: Optional[Node],
    field_name: str,
    comparison: str,
    value: Union[str, float, int]
) -> Optional[Node]:

    if data is None:
        return None

    #A different way of accessing the names
    field_value = getattr(data.value, field_name)

    # Skip missing data
    if field_value is None:
        return filter_rows(data.next, field_name, comparison, value)
    #comparisons
    match = False
    if comparison == "equal":
        match = field_value == value
    elif comparison == "less_than":
        match = field_value < value
    elif comparison == "greater_than":
        match = field_value > value

    filtered_next = filter_rows(data.next, field_name, comparison, value)
    if match:
        return Node(data.value, filtered_next)
    else:
        return filtered_next










# ...

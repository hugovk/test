#!/usr/bin/env python
#  encoding: utf-8
import pytablewriter

writer = pytablewriter.MarkdownTableWriter()
# writer = pytablewriter.SpaceAlignedTableWriter()

writer.header_list = ["int", "float", "str", "bool", "mix", "time"]
writer.value_matrix = [
    ["✅", 0.1, "hoge", True, 0, "2017-01-01 03:04:05+0900"],
    [None, -9.9, "", "FALSE", "nan", "2017-01-01 00:00:00+0900"],
    ["🔺", "-2.23", "foo", False, None, "2017-12-23 45:01:23+0900"],
    [None, -9.9, "", "FALSE", "nan", "2017-01-01 00:00:00+0900"],
]
writer.margin = 1  # add a whitespace for both sides of each cell

writer.write_table()

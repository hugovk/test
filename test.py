#!/usr/bin/env python
#  encoding: utf-8
import pytablewriter

from termcolor import colored

writer = pytablewriter.MarkdownTableWriter()
# writer = pytablewriter.SpaceAlignedTableWriter()

writer.header_list = ["Audit", "Value", "Score", "Weight"]
writer.value_matrix = [
    ["First Contentful Paint", "2.3 s", "91", "3"],
    ["First Meaningful Paint", "2.4 s", "89", "1"],
    ["Speed Index", "3.1 s", "93", "4"],
    ["Time to Interactive", "2.5 s", "98", "5"],
    ["First CPU Idle", "2.4 s", "98", "2"],
    ["Estimated Input Latency", "10 ms", "100", "0"],
    ["Eliminate render-blocking resources", "Potential savings of 0 ms", "100", "0"],
    ["Properly size images", "", "100", "0"],
    ["Defer offscreen images", "", "100", "0"],
    ["Minify CSS", "", "100", "0"],
    ["Minify JavaScript", "", "100", "0"],
    ["Defer unused CSS", "Potential savings of 32 KB", "100", "0"],
    ["Efficiently encode images", "", "100", "0"],
    ["Serve images in next-gen formats", "", "100", "0"],
    ["Enable text compression", "Potential savings of 120 KB", "50", "0"],
    ["Preconnect to required origins", "", "100", "0"],
    ["Reduce server response times (TTFB)", "Root document took 1,110 ms", "🔺", "0"],
    ["Avoid multiple page redirects", "", "100", "0"],
    ["Preload key requests", "", "100", "0"],
    ["Use video formats for animated content", "", "100", "0"],
    ["Avoids enormous network payloads", "Total size was 184 KB", "100", "0"],
    [
        "Serve static assets with an efficient cache policy",
        "4 resources found",
        "51",
        "0",
    ],
    ["Avoids an excessive DOM size", "214 nodes", "100", "0"],
    ["Minimize Critical Requests Depth", "5 chains found", "", "0"],
    ["Network Requests", "", "", "0"],
    ["Metrics", "", "", "0"],
    ["User Timing marks and measures", "", "", "0"],
    ["JavaScript execution time", "0.1 s", "100", "0"],
    ["Screenshot Thumbnails", "", "", "0"],
    ["Final Screenshot", "", "", "0"],
    ["Minimizes main-thread work", "0.4 s", "100", "0"],
    ["All text remains visible during webfont loads", "", "✅", "0"],
]

writer.margin = 1  # add a whitespace for both sides of each cell

writer.write_table()


writer.header_list = ["int", "float", "str", "bool", "mix", "time"]
writer.value_matrix = [
    ["✅", 0.1, "hoge", True, 0, "2017-01-01 03:04:05+0900"],
    [None, -9.9, "", "FALSE", "nan", "2017-01-01 00:00:00+0900"],
    ["🔺", "-2.23", "foo", False, None, "2017-12-23 45:01:23+0900"],
    [None, -9.9, "", "FALSE", "nan", "2017-01-01 00:00:00+0900"],
]
writer.margin = 1  # add a whitespace for both sides of each cell

writer.write_table()


writer.header_list = ["int", "float", "str", "bool", "mix", "time"]
writer.value_matrix = [
    [colored("✅", "green"), 0.1, "hoge", True, 0, "2017-01-01 03:04:05+0900"],
    [None, -9.9, "", "FALSE", "nan", "2017-01-01 00:00:00+0900"],
    [colored("🔺", "red"), "-2.23", "foo", False, None, "2017-12-23 45:01:23+0900"],
    [None, -9.9, "", "FALSE", "nan", "2017-01-01 00:00:00+0900"],
]
writer.margin = 1  # add a whitespace for both sides of each cell

writer.write_table()

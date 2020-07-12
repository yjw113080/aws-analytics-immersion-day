#!/usr/bin/env python3

from aws_cdk import core

from data_analytics_system.data_analytics_system_stack import DataAnalyticsSystemStack


app = core.App()
DataAnalyticsSystemStack(app, "data-analytics-system")

app.synth()

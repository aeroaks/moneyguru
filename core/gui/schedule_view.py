# Created By: Virgil Dupras
# Created On: 2010-01-09
# Copyright 2015 Hardcoded Software (http://www.hardcoded.net)
#
# This software is licensed under the "GPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/gpl-3.0.html

import weakref

from hscommon.trans import tr
from ..const import PaneType
from .base import BaseView, MESSAGES_EVERYTHING_CHANGED
from .schedule_table import ScheduleTable
from .schedule_panel import SchedulePanel

class ScheduleView(BaseView):
    VIEW_TYPE = PaneType.Schedule
    PRINT_TITLE_FORMAT = tr('Schedules from {start_date} to {end_date}')
    INVALIDATING_MESSAGES = (
        MESSAGES_EVERYTHING_CHANGED |
        {'schedule_changed', 'schedule_deleted', 'account_deleted'}
    )

    def __init__(self, mainwindow):
        BaseView.__init__(self, mainwindow)
        self.table = ScheduleTable(self)
        self.columns = self.table.columns
        self.bind_messages(self.INVALIDATING_MESSAGES, self._revalidate)

    def _revalidate(self):
        self.table.refresh_and_show_selection()

    # --- Override
    def save_preferences(self):
        self.table.columns.save_columns()

    # --- Public
    def new_item(self):
        schedule_panel = SchedulePanel(self.mainwindow)
        schedule_panel.view = weakref.proxy(self.view.get_panel_view(schedule_panel))
        schedule_panel.new()
        return schedule_panel

    def edit_item(self):
        schedule_panel = SchedulePanel(self.mainwindow)
        schedule_panel.view = weakref.proxy(self.view.get_panel_view(schedule_panel))
        schedule_panel.load()
        return schedule_panel

    def delete_item(self):
        self.table.delete()


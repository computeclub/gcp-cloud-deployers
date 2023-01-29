# -*- coding: utf-8 -*-
from __future__ import annotations
from clouddeploy_notifier.settings import BaseNotifierSettings


class NotifierSettings(BaseNotifierSettings):

    """
    Application specific settings.
    """

    app_name: str = "release-auto-promoter"


settings = NotifierSettings()  # type: ignore
from __future__ import annotations

import subprocess
import time
from datetime import timedelta
from functools import partial
from pathlib import Path
from typing import Optional, Union

from mac_notifications import client


def join_zoom_meeting(conf_number: Union[int, str]) -> None:
    """Join the zoom meeting"""
    subprocess.run(f'open "zoommtg://zoom.us/join?action=join&confno={conf_number}&browser=chrome"', shell=True)
    print(f"Opened zoom into meeting with {conf_number=}.")


def create_notification_for_meeting(description: str, zoom_conf_number: Optional[str]) -> None:
    """Create a notification for a meeting."""
    path_to_icon = Path(__file__).parent / "zoom.png"
    client.create_notification(
        title="Meeting starts now!",
        subtitle=description,
        icon=path_to_icon,
        callback_timeout=timedelta(seconds=10),
        action_button_str="Join zoom meeting",
        action_callback=partial(join_zoom_meeting, conf_number=zoom_conf_number),
    )
    print(f"Created notification to join meeting {zoom_conf_number} :)")


if __name__ == "__main__":
    print(client.get_notification_manager().get_active_running_notifications())
    create_notification_for_meeting("Standup", "12345678")
    print(client.get_notification_manager().get_active_running_notifications())
    while client.get_notification_manager().get_active_running_notifications() > 0:
        time.sleep(2)
        print(client.get_notification_manager().get_active_running_notifications())

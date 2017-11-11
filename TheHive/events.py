from apps import Event, AppBlueprint
from flask import Blueprint, request

blueprint = AppBlueprint(blueprint=Blueprint('TheHiveEvents', __name__))

hive_event = Event('TheHiveWebHook')


@blueprint.blueprint.route('/thehive_webhook', methods=['POST'])
def thehive_webhook():
    data = request.get_json()
    print("Received data")
    print(data)
    hive_event.trigger(data)
    return 'Success'

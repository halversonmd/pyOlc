from slackclient import SlackClient

slack_token = '8cxLGPzsFwWKDxoW24PgFeT3'
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="C0XXXXXX",
  text="Hello from Python! :tada:"
)

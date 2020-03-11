# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext, CardFactory, MessageFactory
from botbuilder.schema import ChannelAccount, Attachment


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    ADAPTIVE_CARD_CONTENT = {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.0",
        "type": "AdaptiveCard",
        "speak": "<speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xml:lang=\"en-US\">Are you <emphasis level=\"moderate\">sure</emphasis> that you want to cancel this transaction?</speak>",
        "body": [
            {
                "type": "Image",
                "url": "https://www.pngitem.com/pimgs/m/175-1758513_thumbs-up-happy-face-free-hd-smiley-transparent.png"
            },
            {
                "type": "TextBlock",
                "text": "Hello and Welcome!",
                "size": "large"
            },
            {
                "type": "TextBlock",
                "text": "*This is an echo chat bot - it simply echos back whatever you type*"
            },
            {
                "type": "TextBlock",
                "text": "Have Fun!",
                "separation": "none"
            }
        ]
    }

    def create_adaptive_card(self) -> Attachment:
        reply = MessageFactory.list([])
        reply.attachments.append(
            CardFactory.adaptive_card(self.ADAPTIVE_CARD_CONTENT))
        return reply

    async def on_message_activity(self, turn_context: TurnContext):
        await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(self.create_adaptive_card())

import {
    INotificationChannel,
    NotificationFactory,
    TNotificationChannel,
} from "./lib/Notification.ts";

import Observable, { IObservable, IObserver } from "./lib/Observar.ts";

class NotificationService extends Observable {
    private channelType: TNotificationChannel;
    private channel: INotificationChannel;
    
    constructor(channelType: TNotificationChannel) {
        super();
        this.channel = NotificationFactory.createChannel(channelType);
        this.channelType = channelType;
    }

    createObserver = (
        data: Omit<IObserver, "id" | "type" | "update">
    ): IObserver => {
        const type = this.channelType;
        return {
            ...data,
            update: this.channel.send,
            type: type,
            id: Math.random().toString(36).slice(2),
        };
    };

    notify(message: string): void {
        super.notify(message, this.channelType);
    }
}

const emailService = new NotificationService("email");

const pushNotService = new NotificationService("push");


const observer2 = pushNotService.createObserver({
    name: "Jane",
});
const emailObserver1 =emailService.createObserver({
    name: "Email User 1",
});

emailService.subscribe([
    emailObserver1
    ,
    emailService.createObserver({
        name: "Email User 2",
    }),
]);

emailService.unsubscribe(emailObserver1);

pushNotService.subscribe(observer2);

emailService.notify("new Email");

pushNotService.notify("new push notification");

import datetime, time
from lib import get_service, get_events

def get_time(event, loc):
    s = event[loc].get('dateTime', event[loc].get('date'))
    return s

def get_hour(event, loc):
    s = get_time(event, loc)
    time = s[11:-6]
    return datetime.datetime.strptime(time, '%X')

def main():
    service = get_service()
    events = get_events(service, n=20)

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = get_time(event, 'start')
        print(start, event['summary'])

    if len(events) > 0:
        first = events[0]
        now = datetime.datetime.strptime(time.strftime('%X'), '%X')
        gap = get_hour(first, 'start') - now
        print('Gap until: ' first['summary'])
        print('{} minutes'.format(gap.total_seconds() / 60))

    for a, b in zip(events[:-1], events[1:]):
        aEnd   = get_hour(a, 'end')
        bStart = get_hour(b, 'start')
        gap = bStart - aEnd

        print('Gap after: ', a['summary'])
        print('{} minutes'.format(gap.total_seconds() / 60))

    #events = create_event(service)
    #print(events)

if __name__ == '__main__':
    main()


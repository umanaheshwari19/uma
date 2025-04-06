import matplotlib.pyplot as plt


tasks = [
    {'task': 'go to sleep at 10pm', 'status': 'pending'},
    {'task': 'clean the house', 'status': 'completed'},
    {'task': 'breakfast ', 'status': 'pending'},
    {'task': 'going to gym', 'status': 'completed'},
    {'task': 'drinking water in the morning', 'status': 'completed'},
    {'task': 'spending time with family', 'status': 'completed'},
]


status_count = {'completed': 0, 'pending': 0}

for task in tasks:
    status_count[task['status']] += 1


statuses = list(status_count.keys())
counts = list(status_count.values())

plt.bar(statuses, counts, color=['green', 'red'])


plt.title('To-Do List Status')
plt.xlabel('Task Status')
plt.ylabel('Number of Tasks')


plt.show()


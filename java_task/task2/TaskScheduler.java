package java_task.task2;
import java.util.PriorityQueue;

public class TaskScheduler {
    /*
      TaskScheduler class that manages a priority queue of tasks
     */

    // Priority queue to hold tasks
    private final PriorityQueue<Task> queue = new PriorityQueue<>();

   // schedules a new task 
    public void scheduleTask(String id, long epochSeconds, String description) {
        long counter = queue.size(); // to maintain insertion order for tasks with same epochSeconds
        Task newTask = new Task(id, epochSeconds, description, counter);
        queue.add(newTask);
    }

    // executes the next task in the queue
    public void executeDueTasks() {

        long currentTime = System.currentTimeMillis()/1000;
        Task nextTask = queue.peek(); // select the task with the earliest time
        Task dummy = new Task("", currentTime, "", 0);
        
        while (nextTask != null
                && nextTask.compareTo(dummy) <= 0) {
            System.out.println("polling task: " + nextTask.getDescription());
            queue.poll(); // remove the executed task from the queue
            nextTask = queue.peek(); // get the next task
        }



    }


    public static void main(String[] args) {

        TaskScheduler scheduler = new TaskScheduler();
        long now = java.time.Instant.now().getEpochSecond();

        scheduler.scheduleTask("t1", now + 2, "Backup database");
        scheduler.scheduleTask("t2", now + 2, "Send report email 1");
        scheduler.scheduleTask("t3", now + 2, "Send report email 2");
        scheduler.scheduleTask("t4", now + 2, "Send report email 3");
        scheduler.scheduleTask("t5", now + 2, "System cleanup");
        scheduler.scheduleTask("late", now - 5, "Run missed task");

        // simple loop
        for (int i = 0; i < 6; i++) {
        scheduler.executeDueTasks();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
                Thread.currentThread().interrupt();
            }
        }

    }
}

class Task implements Comparable<Task> {
    /*
      Task class representing a task given the name, duration and description
     */

    private final String name;
    private long epochSeconds;
    private final String description;
    private long counter = 0;

    public Task(String name, long epochSeconds, String description, long counter) {
        this.name = name;
        this.epochSeconds = epochSeconds;
        this.description = description;
        this.counter = counter;
    }

    public String getDescription() {
        return description;
    }

    @Override
    public int compareTo(Task other) {
        if (this.epochSeconds == other.epochSeconds) {
            return Long.compare(this.counter, other.counter); // compare by counter if times are equal
        }
        else{
            return Long.compare(this.epochSeconds, other.epochSeconds); // compare by epochSeconds
        }
    }
}





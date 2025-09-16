package java_task.task2;
import java.util.PriorityQueue;

public class TaskScheduler {
    /*
      TaskScheduler class that manages a priority queue of tasks
     */

    // Priority queue to hold tasks
    private final PriorityQueue<Task> queue = new PriorityQueue<>();

    public void scheduleTask(String id, long epochSeconds, String description) {
    }

    public void executeNextTask() {
    }

}



class Task implements Comparable<Task> {
    /*
      Task class representing a task given the name, duration and description
     */

    private final String name;
    private long epochSeconds;
    private final String description;

    public Task(String name, long epochSeconds, String description) {
        this.name = name;
        this.epochSeconds = epochSeconds;
        this.description = description;
    }

    @Override
    public String toString() {
        return "name; " + name + " - epochSeconds = " + epochSeconds + "- description = " + description;
    }

    @Override
    public int compareTo(Task other) {
        // compare tasks based on their epochSeconds
        return Long.compare(this.epochSeconds, other.epochSeconds);
    }
}





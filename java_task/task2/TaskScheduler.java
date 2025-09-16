package java_task.task2;
import java.util.PriorityQueue;

public class TaskScheduler {
    /*
      TaskScheduler class that manages a priority queue of tasks
     */

    // Priority queue to hold tasks
    private final PriorityQueue<Task> queue = new PriorityQueue<>();

    // Testing creating Tasks
    public static void main(String[] args) {
    Task task1 = new Task("Task1", 5000, "Description1");
    Task task2 = new Task("Task2", 3000, "Description2");

    //print the tasks
    System.out.println(task1);
    System.out.println(task2);

}

}

class Task implements Comparable<Task> {
    /*
      Task class representing a task given the name, duration and description
     */

    private final String name;
    private long duration;
    private final String description;

    public Task(String name, long duration, String description) {
        this.name = name;
        this.duration = duration;
        this.description = description;
    }

    @Override
    public String toString() {
        return "name; " + name + " - duration = " + duration + "- description = " + description;
    }

    @Override
    public int compareTo(Task other) {
        // compare tasks based on their duration
        return Long.compare(this.duration, other.duration);
    }
}





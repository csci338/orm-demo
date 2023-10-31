import { React, useEffect, useState } from "react";

export default function App() {
    const [taskList, setTaskList] = useState([]);

    async function getTasks() {
        const response = await fetch("/api/tasks");
        const tasks = await response.json();
        console.log(tasks);
        setTaskList(tasks);
    }

    useEffect(() => {
        getTasks();
    }, []);

    return (
        <main>
            <section>
                <h2>Task List</h2>
                {taskList.map((task) => {
                    return (
                        <div className="item">
                            <strong>{task.name}</strong>
                            <p>{task.description}</p>
                        </div>
                    );
                })}
            </section>
        </main>
    );
}

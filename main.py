import tasks
import search
import storage
import interface


def main():
    tasks.tasks = storage.load_tasks()

    print("\nWelcome to Task Scheduler!")

    while True:
        interface.show_menu()

        choice = interface.get_choice()

        if choice == 1:
            tasks.add_task()
            storage.save_tasks(tasks.tasks)

        elif choice == 2:
            tasks.view_tasks()

        elif choice == 3:
            tasks.complete_task()
            storage.save_tasks(tasks.tasks)

        elif choice == 4:
            tasks.delete_task()
            storage.save_tasks(tasks.tasks)

        elif choice == 5:
            tasks.change_priority()
            storage.save_tasks(tasks.tasks)

        elif choice == 6:
            keyword = interface.get_keyword()
            results = search.search_task(tasks.tasks, keyword)
            interface.display_results(results)

        elif choice == 7:
            priority, status = interface.get_filter()

            if priority is not None or status is not None:
                results = search.filter_tasks(
                    tasks.tasks,
                    priority,
                    status
                )

                interface.display_results(results)

        elif choice == 8:
            search.print_statistics(tasks.tasks)

        elif choice == 9:
            storage.save_tasks(tasks.tasks)
            print("Tasks saved.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
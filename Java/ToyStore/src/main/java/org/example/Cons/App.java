package org.example.Cons;

import org.example.Configs.Config;
import org.example.Core.MVP.Presenter;
import org.example.Core.Models.Toy;

import java.util.Scanner;

@SuppressWarnings("ALL")
public class App {
    public static void buttonClick() {
        Presenter presenter = new Presenter(new ConsoleView(), Config.pathDb);
        presenter.loadFromFile();

        String command;

        while (true) {

            command = prompt("""

                     1 - Добавьте игрушку
                     2 - Удалить игрушку
                     3 - Розыгрыш игрушек
                     4 - Cписок игрушек
                     5 - Очистить все записи
                     6 - Сохраните все записи в файл
                     7 - Загрузите все записи из файла
                     8 - Выход
                    Ввод:\s""");
            if (command.equals("8")) {
                return;
            }
            try {
                switch (command) {
                    case "1" -> presenter.putForRaffle();
                    case "2" -> presenter.deleteFromRaffle();
                    case "3" -> presenter.getRaffle();
                    case "4" -> presenter.showAll();
                    case "5" -> presenter.clearAll();
                    case "6" -> presenter.saveToFile();
                    case "7" -> presenter.loadFromFile();
                    default -> System.out.println("\n Не верный ввод команды!");
                }
            } catch (Exception e) {
                System.out.println("Error. " + e.getMessage());
            }
        }
    }

    private static String prompt(String message) {
        Scanner in = new Scanner(System.in);
        System.out.print(message);
        return in.nextLine();
    }

    private static Toy toyCreate() {
        int id = Integer.parseInt(prompt("Id игрушки: "));
        String name = prompt("Название игрушки: ");
        String weight = prompt("Вес игрушки: ");
        return (new Toy(id, name, Integer.parseInt(weight)));
    }
}
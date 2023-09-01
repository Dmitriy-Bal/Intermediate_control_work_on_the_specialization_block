package org.example.Cons;

import org.example.Configs.Config;
import org.example.Core.MVP.IView;
import org.example.Core.Models.Toy;

import java.util.List;
import java.util.Scanner;

public class ConsoleView implements IView {
    Scanner in;

    public ConsoleView() {
        in = new Scanner(System.in);
    }

    @Override
    public int getToyId() {
        System.out.print("Id игрушки: ");
        return Integer.parseInt(in.nextLine());
    }

    @Override
    public String getToyNaming() {
        System.out.print("Название игрушки: ");
        return in.nextLine();
    }

    @Override
    public int getToyWeight() {
        System.out.print("Вес игрушки: ");
        return Integer.parseInt(in.nextLine());
    }

    @Override
    public void showAll(List<Toy> toys) {
        System.out.println("\nСписок игрушек:");
        for (Toy toy : toys) {
            System.out.println(toy);
        }
    }


    @Override
    public void showGetToy(Toy toy) {
        System.out.print("\nРезультат розыгрыша: \n");
        System.out.println(toy);
    }

    @Override
    public void loadMessage() {
        System.out.println("\nФайл загружен в текущую сессию");
    }

    @Override
    public boolean clearAllDecision() {
        boolean f = false;
        System.out.print("\nУдалить все записи? Необходимо подтверждение: (y/n): ");
        if (in.nextLine().equalsIgnoreCase("Y")) {
            f = true;
        }
        return f;
    }

    @Override
    public void savedAll() {
        System.out.println("\nЗаписи сохранены в файл: " + Config.pathDb);
    }

    @Override
    public void savedItem() {
        System.out.println("\nИгрушка успешно добавлена!");
    }

    @Override
    public void saveError() {
        System.out.println("\nОшибка. Добавить не удалось");
    }

    @Override
    public void emptyListMessage() {
        System.out.println("Отсутствует информация об игрушках!");
    }

    @Override
    public int getRaffleTimes() {
        System.out.print("Укажите количество, сколько раз вы хотите играть: ");
        return Integer.parseInt(in.nextLine());
    }
}
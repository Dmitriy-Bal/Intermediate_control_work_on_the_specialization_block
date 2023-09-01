package org.example.Core.MVP;

import org.example.Configs.Config;
import org.example.Core.Models.Toy;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class Presenter {
    private final Model model;
    private final IView view;

    public Presenter(IView view, String pathDb) {
        this.view = view;
        model = new Model(pathDb);
    }

    public void loadFromFile() {
        model.load();
        view.loadMessage();
    }

    public void putForRaffle() {
        if (model.currentToys().putForRaffle(
                new Toy(view.getToyId(), view.getToyNaming(), view.getToyWeight())))
            view.savedItem();
        else
            view.saveError();
    }

    public void deleteFromRaffle() {
        if (model.currentToys.getToys().size() == 0)
            view.emptyListMessage();
        else
            model.currentToys().removeToy(view.getToyId());
    }

    public void saveToFile() {
        model.save();
        view.savedAll();
    }

    public void showAll() {
        if (model.currentToys.getToys().size() == 0)
            view.emptyListMessage();
        else
            view.showAll(model.currentToys.getToys());
    }

    public void clearAll() {
        if (model.currentToys.getToys().size() == 0)
            view.emptyListMessage();
        else {
            if (view.clearAllDecision()) {
                model.currentToys.getToys().clear();
                System.out.println("Удаление прошло успешно!");
            }
        }
    }


    public void getRaffle() {
        Toy raffleToy;
        List<Toy> raffleToys = new ArrayList<>();
        List<Toy> winsToys = new ArrayList<>();
        int size = model.currentToys.getToys().size();
        if (size != 0) {
            int times = view.getRaffleTimes();
            List<Toy> currentToys = model.currentToys.getToys();
            for (Toy toy : currentToys) {
                for (int i = 0; i < toy.getWeight(); i++) {
                    raffleToys.add(toy);
                }
            }
            for (int i = 0; i < times; i++) {
                Random random = new Random();
                int randomIndex = random.nextInt(raffleToys.size());
                raffleToy = raffleToys.get(randomIndex);
                view.showGetToy(raffleToy);
                winsToys.add(raffleToy);
            }
            model.saveResult(Config.pathResult, winsToys);
        } else
            view.emptyListMessage();
    }
}
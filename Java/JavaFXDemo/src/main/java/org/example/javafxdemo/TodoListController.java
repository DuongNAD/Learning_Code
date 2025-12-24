package org.example.javafxdemo;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;

import javafx.event.ActionEvent;

public class TodoListController {
    @FXML
    private Label lbTodoList;

    @FXML
    private TextField txInputTodoList;

    @FXML
    private ListView<String> ListViewTodoList;

    @FXML
    private Button btnAddTodoList;

    @FXML
    private Button btnRemoveTodoList;

    @FXML
    protected void onAdd(ActionEvent event) {
        String todoItem = txInputTodoList.getText();
        if(todoItem != null && !todoItem.trim().isEmpty()){
            ListViewTodoList.getItems().add(todoItem);
        }
        txInputTodoList.clear();
    }

    @FXML
    protected void onRemove(ActionEvent event) {
        String selectedItem = ListViewTodoList.getSelectionModel().getSelectedItem();
        if (selectedItem != null) {
            ListViewTodoList.getItems().remove(selectedItem);
        }
    }
}

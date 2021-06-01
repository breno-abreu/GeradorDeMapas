package ptg;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import ptg.generators.Map;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.Objects;

public class Controller {
    @FXML
    ImageView imageView;
    @FXML
    private TextField seedField;
    @FXML
    private TextField freqField;
    @FXML
    private TextField octField;
    @FXML
    private TextField layerElevationField1;
    @FXML
    private TextField layerElevationField2;
    @FXML
    private TextField layerElevationField3;
    @FXML
    private TextField layerElevationField4;
    @FXML
    private TextField layerElevationField5;
    @FXML
    private TextField layerElevationField6;
    @FXML
    private TextField layerElevationField7;
    @FXML
    private TextField layerColorField1;
    @FXML
    private TextField layerColorField2;
    @FXML
    private TextField layerColorField3;
    @FXML
    private TextField layerColorField4;
    @FXML
    private TextField layerColorField5;
    @FXML
    private TextField layerColorField6;
    @FXML
    private TextField layerColorField7;

    private Stage primaryStage;
    private final Map map;

    public Controller(){
        map = new Map();
    }

    public void generateMap(ActionEvent e){
        try {
            map.generateNoiseMap(Long.parseLong(seedField.getText()), Double.parseDouble(freqField.getText()), Integer.parseInt(octField.getText()));
            map.setLayers(0, Double.parseDouble(layerElevationField1.getText()), layerColorField1.getText());
            map.setLayers(1, Double.parseDouble(layerElevationField2.getText()), layerColorField2.getText());
            map.setLayers(2, Double.parseDouble(layerElevationField3.getText()), layerColorField3.getText());
            map.setLayers(3, Double.parseDouble(layerElevationField4.getText()), layerColorField4.getText());
            map.setLayers(4, Double.parseDouble(layerElevationField5.getText()), layerColorField5.getText());
            map.setLayers(5, Double.parseDouble(layerElevationField6.getText()), layerColorField6.getText());
            map.setLayers(6, Double.parseDouble(layerElevationField7.getText()), layerColorField7.getText());
            map.generateElevationMap();
            displayImage();
        }
        catch(Exception ex) {
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("ATENÇÃO");
            alert.setHeaderText(null);
            alert.setContentText(ex.getMessage());
            alert.showAndWait();
        }
    }

    public void displayImage(){
        try {
            File img = new File("temp/map.png");
            InputStream image = (InputStream) new FileInputStream(img);
            imageView.setImage(new Image(image));
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
    }

    public void saveFile(){
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Save");
        fileChooser.getExtensionFilters().addAll(new FileChooser.ExtensionFilter("PNG", "*.png"));
        File file = fileChooser.showSaveDialog(primaryStage);
        map.saveMap(file.getAbsolutePath());
    }

    public void setPrimaryStage(Stage primaryStage){
        this.primaryStage = primaryStage;
    }
}

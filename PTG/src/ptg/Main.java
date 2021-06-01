package ptg;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import ptg.generators.*;
import java.awt.*;
import java.io.File;
import java.util.Objects;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("ptg.fxml")));
            Image icon = new Image("perlin_color.png");
            Controller controller = new Controller();
            controller.setPrimaryStage(primaryStage);
            primaryStage.getIcons().add(icon);
            primaryStage.setTitle("Procedural Terrain Generator");
            primaryStage.setScene(new Scene(root, 1200, 850));
            primaryStage.setResizable(false);
            primaryStage.show();
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
    }

    public static void main(String[] args) {
        File dir = new File("temp");
        boolean aux = dir.mkdir();
        launch(args);
    }
}

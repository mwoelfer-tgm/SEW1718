import java.io.IOException;
import java.net.ServerSocket;

public class CalculatorServer {
    private int port;
    private boolean running;
    private ServerSocket serverSocket;

    public CalculatorServer(int port) throws IOException{
        this.port = port;
        this.running = true;
        this.serverSocket = new ServerSocket(this.port);
    }

    public void bind() {
        while (this.running){

        }
    }

    public void stop() throws IOException{
        this.running = false;
        this.serverSocket.close();
    }

    public static void main(String[] args){
        CalculatorServer server = new CalculatorServer(12345);
        server.bind();
    }
}

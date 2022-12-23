import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;

public class Client {
    public static void main(String[] args) {
        try {
            // Créez un socket en mode UDP
            DatagramSocket socket = new DatagramSocket();

            while (true) {
                try {
                    // Demandez à l'utilisateur de taper une commande
                    System.out.println("Action du joueur :");
                    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
                    String command = reader.readLine();

                    // Envoyez la commande au serveur
                    byte[] data = command.getBytes();
                    InetAddress address = InetAddress.getByName("localhost");
                    int port = 5000;
                    DatagramPacket packet = new DatagramPacket(data, data.length, address, port);
                    socket.send(packet);

                    // Recevez une réponse du serveur
                    byte[] buffer = new byte[1024];
                    packet = new DatagramPacket(buffer, buffer.length);
                    socket.receive(packet);
                    String response = new String(packet.getData(), 0, packet.getLength());
                    System.out.println("Réponse du serveur : " + response);
                } catch (SocketException e) {
                    // Si la connexion est interrompue, fermez le socket et arrêtez le programme
                    System.out.println("La connexion a été interrompue, arrêt du programme.");
                    socket.close();
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        try {
            // Créez un socket en mode UDP
            DatagramSocket socket = new DatagramSocket(5002); // Utilisez le port 5002
            while (true) {
                try {
                    // Demandez à l'utilisateur de taper une commande
                    System.out.println("Action du joueur :");
                    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
                    String command = reader.readLine();

                    // Envoyez la commande au middleware
                    byte[] data = command.getBytes();
                    InetAddress address = InetAddress.getByName("localhost");
                    int port = 5001; // Port du middleware
                    DatagramPacket packet = new DatagramPacket(data, data.length, address, port);
                    socket.send(packet);

                    // Recevez une réponse du serveur
                    try {
                    // Recevez une réponse du serveur
                    byte[] buffer = new byte[1024];
                    DatagramPacket packet3 = new DatagramPacket(buffer, buffer.length);
                    socket.receive(packet3);
                    String response = new String(packet3.getData(), 0, packet3.getLength());
                    System.out.println("Réponse du serveur : " + response);} catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                    try {
                        // Recevez une réponse du middleware
                        byte[] buffer2 = new byte[1024];
                        DatagramPacket packet2 = new DatagramPacket(buffer2, buffer2.length);
                        socket.receive(packet2);
                        String response2 = new String(packet2.getData(), 0, packet2.getLength());
                        System.out.println("Réponse du middleware : " + response2);
                    } catch (IOException e) {
                        System.out.println("La connexion a été interrompue, arrêt du programme.");
                        socket.close();
                        break;
                    }
                } catch (SocketException e) {
                    // Si la connexion a été interrompue, quittez la boucle
                    System.out.println("La connexion a été interrompue, arrêt du programme.");
                    socket.close();
                    break;
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }


        } catch (SocketException e) {
            // Si la connexion est interrompue, fermez le socket et arrêtez le programme
            System.out.println("La connexion a été interrompue, arrêt du programme.");

        }
    }
}

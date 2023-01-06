import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws SocketException {
        // Création du socket du client
        DatagramSocket socket = new DatagramSocket(6000);

        // Création du scanner pour lire les entrées de l'utilisateur
        Scanner scanner = new Scanner(System.in);

        // Démarrage d'un thread pour écouter les réponses du middleware
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    while (true) {
                        // Création d'un paquet de données pour recevoir les réponses du middleware
                        byte[] receiveData = new byte[1024];
                        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

                        // Réception du paquet de données
                        socket.receive(receivePacket);

                        // Récupération de la réponse du middleware
                        String response = new String(receivePacket.getData(), 0, receivePacket.getLength());

                        // Affichage de la réponse sur la console
                        System.out.println(response);
                        if (response.contains("voici la taille du mot")) {
                            System.out.println("Veuillez saisir le mot cherché : ");
                            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
                            String command = reader.readLine();

                            // Envoi de la commande au middleware
                            byte[] data = command.getBytes();
                            InetAddress address = InetAddress.getByName("localhost");
                            int port = 6002; // Port du middleware
                            DatagramPacket packet = new DatagramPacket(data, data.length, address, port);
                            socket.send(packet);
                            return;
                        }
                        System.out.println("Saisir :");
                        socket.receive(receivePacket);
                        // Récupération de la réponse du middleware
                        String response2 = new String(receivePacket.getData(), 0, receivePacket.getLength());
                        System.out.println(response2);


                    }
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }).start();


        try {
            while (true) {
                // Demande à l'utilisateur de taper une commande
                System.out.println("Action du joueur :");
                BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
                String command = reader.readLine();

                // Envoi de la commande au middleware
                byte[] data = command.getBytes();
                InetAddress address = InetAddress.getByName("localhost");
                int port = 6002; // Port du middleware
                DatagramPacket packet = new DatagramPacket(data, data.length, address, port);
                socket.send(packet);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}

# Opty Socket Client

Traditional Java Socket client for the Opty chat system.

## 📁 Project Structure

```
opty-socket-client/
├── src/                        # Source code
│   ├── ClienteChat.java        # Main application
│   ├── Parceiro.java           # Socket wrapper
│   ├── TratadoraDeMensagens.java  # Message handler thread
│   └── com/opty/socket/tradicional/comunicado/
│       ├── Comunicado.java
│       ├── PedidoDeConexao.java
│       ├── RespostaDeConexao.java
│       ├── MensagemTexto.java
│       ├── PedidoParaSair.java
│       └── ComunicadoDeDesligamento.java
│
├── build/                      # Compiled classes (auto-generated)
├── scripts/
│   └── run.sh                  # Build and run script
└── README.md
```

## 🚀 Quick Start

```bash
# Run client (auto-compiles if needed)
./scripts/run.sh

# Connect to a specific host/port
./scripts/run.sh localhost 3000
./scripts/run.sh 192.168.1.100 3000
```

## 📌 Requirements

* Java 17+
* Server running on port 3000 (default)

## ✨ Features

* Traditional Java Socket communication
* Real-time chat with supervisors
* Automatic reconnection support
* Session management
* Graceful disconnect handling

## 🧱 Architecture

Follows the professor’s exact communication pattern:

* **Socket**: Standard TCP socket (not WebSocket)
* **Serialization**: `ObjectInputStream` / `ObjectOutputStream`
* **Threads**: Manual thread management (`extends Thread`)
* **Parceiro**: Socket wrapper with `espie()`, `envie()`, `receba()`
* **Comunicados**: Serializable message objects

## 🔌 How It Works

1. Client connects to the server via TCP socket
2. Creates `ObjectOutputStream` (with flush to avoid deadlocks)
3. Creates `ObjectInputStream`
4. Sends `PedidoDeConexao`
5. Receives `RespostaDeConexao` with `sessionId`
6. Starts `TratadoraDeMensagens` thread to process incoming messages
7. Main thread reads user input and sends messages
8. On exit, sends `PedidoParaSair`

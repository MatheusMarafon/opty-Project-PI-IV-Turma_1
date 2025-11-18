/* --- IMPORTS --- */
import { useEffect, useRef, useState, useCallback } from 'react';


/* --- TYPES --- */
// WebSocket message structure
export interface WebSocketMessage {
  /*
  * Example message structure:
  * {
  *   "sessionId": "abc123",
  *   "from": "SERVER",
  *   "type": "MESSAGE",
  *   "payload": {
  *     "content": "Hello, World!"
  *   },
  *   "timestamp": "2025-01-01T12:00:00Z"
  * }
  */
  sessionId: string | null;
  from: string;
  type: 'CONNECT' | 'MESSAGE' | 'DISCONNECT' | 'PING' | 'PONG' | 'ERROR';
  payload?: Record<string, unknown>;
  timestamp?: string;
}

// WebSocket hook options
export interface UseWebSocketOptions {

  // WebSocket server URL
  url: string;

  // Callback functions
  onOpen?: () => void;
  onMessage?: (message: WebSocketMessage) => void;
  onClose?: () => void;
  onError?: (error: Event) => void;

  // Reconnection settings
  reconnect?: boolean;
  reconnectInterval?: number;
  maxReconnectAttempts?: number;

  // Whether to establish the connection immediately
  shouldConnect?: boolean;
}

// WebSocket hook return type
export interface UseWebSocketReturn {

  // Send a message through the WebSocket
  sendMessage: (message: WebSocketMessage) => void;

  // Disconnect the WebSocket
  disconnect: () => void;

  // Connection status
  isConnected: boolean;

  // Last received message
  lastMessage: WebSocketMessage | null;
}


/* --- CODE --- */
export const useWebSocket = ({
  url,
  onOpen,
  onMessage,
  onClose,
  onError,
  reconnect = true,
  reconnectInterval = 3000,
  maxReconnectAttempts = 5,
  shouldConnect = true,
}: UseWebSocketOptions): UseWebSocketReturn => {

  // Define refs and state
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimeoutRef = useRef<NodeJS.Timeout>();
  const reconnectAttemptsRef = useRef(0);
  const [isConnected, setIsConnected] = useState(false);
  const [lastMessage, setLastMessage] = useState<WebSocketMessage | null>(null);
  const shouldReconnectRef = useRef(true);
  const isConnectingRef = useRef(false);

  // Function to establish WebSocket connection
  const connect = useCallback(() => {

    // Prevent multiple connections
    if (wsRef.current?.readyState === WebSocket.OPEN || wsRef.current?.readyState === WebSocket.CONNECTING || isConnectingRef.current) {
      return;
    }

    // Create WebSocket connection
    try {

      // Indicate that we are in the process of connecting
      isConnectingRef.current = true;

      // Create WebSocket instance
      const ws = new WebSocket(url);

      // Connection successful
      ws.onopen = () => {

        // Define connection state
        isConnectingRef.current = false;
        setIsConnected(true);

        // Reset reconnection attempts
        reconnectAttemptsRef.current = 0;
        onOpen?.();
      };

      // Handle incoming messages
      ws.onmessage = (event) => {
        try {

          // Parse message
          const message: WebSocketMessage = JSON.parse(event.data);
          setLastMessage(message);

          // Incoming message is a PING: respond with PONG
          if (message.type === 'PING') {

            // Send PONG response
            const pongMessage: WebSocketMessage = {
              sessionId: message.sessionId,
              from: 'CLIENT',
              type: 'PONG',
            };

            // Send PONG response
            ws.send(JSON.stringify(pongMessage));
          }

          // Invoke message callback
          onMessage?.(message);
        
          
        }

        // Handler with parsing errors
        catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      // Handle connection closure
      ws.onclose = (event) => {

        // Log disconnection
        console.log('WebSocket disconnected', event.code, event.reason);

        // Update connection state
        isConnectingRef.current = false;
        setIsConnected(false);

        // Clear WebSocket ref
        wsRef.current = null;

        // Invoke close callback
        onClose?.();

        // Only reconnect if it was an unexpected closure and we should reconnect
        const wasCleanClose = event.code === 1000;

        // Attempt reconnection if needed
        if (!wasCleanClose && shouldReconnectRef.current && reconnect && reconnectAttemptsRef.current < maxReconnectAttempts) {

          // Increment reconnection attempts
          reconnectAttemptsRef.current += 1;

          // Log reconnection attempt
          console.log(`Attempting reconnection (${reconnectAttemptsRef.current}/${maxReconnectAttempts})...`);

          // Schedule reconnection
          reconnectTimeoutRef.current = setTimeout(connect, reconnectInterval);
        }

        // Log clean close
        else if (wasCleanClose) {
          console.log('Clean close, not reconnecting');
        }
      };

      // Handle errors
      ws.onerror = (error) => {

        // Log error
        console.error('WebSocket error:', error);

        // Define connection state
        isConnectingRef.current = false;

        // Invoke error callback
        onError?.(error);
      };

      // Save WebSocket instance
      wsRef.current = ws;

    } catch (error) {
      // Log error
      console.error('Error creating WebSocket:', error);

      // Define connection state
      isConnectingRef.current = false;
    }
  }, [url, onOpen, onMessage, onClose, onError, reconnect, reconnectInterval, maxReconnectAttempts]);


  // Function to send a message through the WebSocket
  const sendMessage = useCallback((message: WebSocketMessage) => {

    // Check if WebSocket is open before sending
    if (wsRef.current?.readyState === WebSocket.OPEN) {

      // Send the message
      wsRef.current.send(JSON.stringify(message));
    
    // WebSocket not connected: log failed
    } else {
      console.warn('WebSocket is not connected. Message not sent:', message);
    }
  }, []);


  // Function to disconnect the WebSocket
  const disconnect = useCallback(() => {

    // Set flag to prevent reconnection
    shouldReconnectRef.current = false;

    // Clear any pending reconnection attempts
    if (reconnectTimeoutRef.current) {

      // Clear timeout
      clearTimeout(reconnectTimeoutRef.current);
    }

    // Close WebSocket connection
    if (wsRef.current) {

      // Close the WebSocket
      wsRef.current.close();

      // Clear WebSocket ref
      wsRef.current = null;
    }
  }, []);


  // Effect to manage connection lifecycle
  useEffect(() => {

    // Establish connection if needed
    if (shouldConnect) {
      connect();
    }

    return () => {

      // On unmount, prevent reconnection and close WebSocket
      shouldReconnectRef.current = false;

      // Clear any pending reconnection attempts
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current);
      }

      // Close WebSocket connection
      if (wsRef.current) {
        wsRef.current.close();
        wsRef.current = null;
      }
    };
  }, [connect, shouldConnect]);


  // Return WebSocket API
  return {
    sendMessage,
    disconnect,
    isConnected,
    lastMessage,
  };
};

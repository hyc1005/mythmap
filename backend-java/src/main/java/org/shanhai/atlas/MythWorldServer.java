package org.shanhai.atlas;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.concurrent.Executors;

public final class MythWorldServer {
    private MythWorldServer() {}

    public static void main(String[] args) throws IOException {
        String configuredPath = System.getenv().getOrDefault("MYTH_WORLD_PATH", "frontend/public/data/myth-world.json");
        Path worldPath = Path.of(args.length > 0 ? args[0] : configuredPath).toAbsolutePath().normalize();
        int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8081"));
        HttpServer server = HttpServer.create(new InetSocketAddress("127.0.0.1", port), 0);
        server.createContext("/health", exchange -> respond(exchange, 200, "application/json; charset=utf-8", "{\"status\":\"ok\",\"service\":\"myth-world-java\"}".getBytes(StandardCharsets.UTF_8)));
        server.createContext("/api/world", exchange -> serveWorld(exchange, worldPath));
        server.setExecutor(Executors.newFixedThreadPool(Math.max(4, Runtime.getRuntime().availableProcessors())));
        server.start();
        System.out.printf("Myth world API listening on http://localhost:%d; data=%s%n", port, worldPath);
    }

    private static void serveWorld(HttpExchange exchange, Path worldPath) throws IOException {
        if (!exchange.getRequestURI().getPath().equals("/api/world")) {
            respond(exchange, 404, "application/json; charset=utf-8", "{\"error\":\"not found\"}".getBytes(StandardCharsets.UTF_8));
            return;
        }
        if (!exchange.getRequestMethod().equals("GET")) {
            exchange.getResponseHeaders().set("Allow", "GET, OPTIONS");
            respond(exchange, 405, "application/json; charset=utf-8", "{\"error\":\"method not allowed\"}".getBytes(StandardCharsets.UTF_8));
            return;
        }
        if (!Files.isRegularFile(worldPath)) {
            respond(exchange, 500, "application/json; charset=utf-8", "{\"error\":\"world data file is unavailable\"}".getBytes(StandardCharsets.UTF_8));
            return;
        }
        respond(exchange, 200, "application/json; charset=utf-8", Files.readAllBytes(worldPath));
    }

    private static void respond(HttpExchange exchange, int status, String contentType, byte[] body) throws IOException {
        exchange.getResponseHeaders().set("Content-Type", contentType);
        exchange.getResponseHeaders().set("Cache-Control", "no-cache");
        exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
        exchange.getResponseHeaders().set("Access-Control-Allow-Methods", "GET, OPTIONS");
        exchange.getResponseHeaders().set("Access-Control-Allow-Headers", "Content-Type");
        if (exchange.getRequestMethod().equals("OPTIONS")) {
            exchange.sendResponseHeaders(204, -1);
            exchange.close();
            return;
        }
        exchange.sendResponseHeaders(status, body.length);
        try (var output = exchange.getResponseBody()) {
            output.write(body);
        }
    }
}

package dev.campuslands;

import java.util.Map;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class App {
  public static void main(String[] args) {
    SpringApplication.run(App.class, args);
  }
}

@RestController
class HomeController {
  private final JdbcTemplate jdbc;
  HomeController(JdbcTemplate jdbc) { this.jdbc = jdbc; }
  @GetMapping("/")
  Map<String, Object> home() {
    String now = jdbc.queryForObject("select now()::text", String.class);
    return Map.of("stack", "Spring Boot + PostgreSQL", "dbTime", now);
  }
}

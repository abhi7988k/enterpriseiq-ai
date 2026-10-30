package EnterpriseIQ.controller;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/test")
public class TestController {

    @PostMapping("secure")
    public String secure(){
        return "Authenticated Successfully";
    }

    @GetMapping("/admin")
    public String admin() {
        return "Admin access granted";
    }
}

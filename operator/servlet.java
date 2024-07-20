import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.PrintWriter;

public class WearMaskServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Set response content type
        response.setContentType("text/html");

        // Get the response writer
        PrintWriter out = response.getWriter();

        // Write the response
        out.println("<html><body>");
        out.println("<h1>Wear Mask</h1>");
        out.println("</body></html>");
    }
}

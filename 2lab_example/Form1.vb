Public Class Form1
    Dim n, glob As Integer
    Private Sub Button1_Click(sender As Object, e As EventArgs)
        REM    WebBrowser1.Url = New Uri("https://moodle.anantchenko.ru/admin/cron.php?password=111")

    End Sub

    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        If n = 0 Then
            Label2.Text = glob
            WebBrowser1.Url = New Uri("https://www.yandex.ru")
        End If
        n = n + 1
        If n = 10 Then glob = glob + 1 : n = 0

    End Sub
End Class

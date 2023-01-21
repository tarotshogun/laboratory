Attribute VB_Name = "CaseXMLHTTP60"
' @breif A case for using `XMLHTTP60`
' @note This cannot support content that is loaded by Javascript.
'       https://qiita.com/asamiKA/items/3944ba300ba5341762c8
' @remark  "Microsoft Html Object Library" must be added from the reference settings
Sub CaseXMLHTTP60()

    Dim http As MSXML2.XMLHTTP60
    Set http = New MSXML2.XMLHTTP60
    
    Call http.Open("GET", "https://www.yahoo.co.jp/", False)
    Call http.send
    
    Do While http.readyState <> 4
      DoEvents
    Loop

    Dim document As Object
    Set document = New MSHTML.HtmlDocument
    Call document.Write(http.responseText)
    
    Debug.Print document.body.innerHTML
    Debug.Print document.getElementsByTagName("article")(0).innerText
    
    Set http = Nothing
    Set document = Nothing

End Sub


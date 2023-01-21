Attribute VB_Name = "CaseHtmlDocument"
' @breif A case for using `HtmlDocument`
' @note This cannot support content that is loaded by Javascript.
'       https://qiita.com/asamiKA/items/3944ba300ba5341762c8
' @remark  "Microsoft Html Object Library" must be added from the reference settings
Sub CaseHtmlDocument()

    Dim html As MSHTML.HtmlDocument
    Set html = New MSHTML.HtmlDocument
    
    Dim document As MSHTML.HtmlDocument
    Set document = html.createDocumentFromUrl("http://example.com/", vbNullString)
    
    Do While document.readyState <> "complete"
        DoEvents
    Loop
    
    Debug.Print document.body.innerHTML
    Debug.Print document.getElementsByTagName("h1")(0).innerText
    
    Set html = Nothing
    Set document = Nothing

End Sub



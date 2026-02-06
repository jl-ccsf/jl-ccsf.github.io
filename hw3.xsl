<?xml version="1.0" encoding="UTF-8"?>
<!--JULES LENZI 02/05/2026-->
<!--Client Accounts Ledger Template-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" version="5.0" encoding="UTF-8"/>    
    <xsl:template match="/">
        <!--XHTML-->
        <html lang="en">
            <head>
                <title>Homework 3: XSL Transformation</title>
                <!--META-->
                <meta name="description" content="XSLT practice for CNIT-131A at CCSF, Spring 2026"/>
                <meta name="keywords" content="XML, XSLT, HTML, CSS, CCSF, student"/>
                <meta name="author" content="Jules Lenzi"/>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                <!--CSS-->
                <link rel="stylesheet" href="hw3.css"/>
            </head>
            <body>
                <div class="content">
                    <!--NAV-->
                    <nav>
                        <a href="https://jl-ccsf.github.io/cnit131a.html" title="All assignments" id="home">
                            <button id="return">&lt; Directory</button>
                        </a>
                    </nav>
                    <br/>
                    <!--MAIN-->
                    <main>
                        <h1>List of Clients</h1>                    
                        <table>
                            <tr id="top-row">
                                <th>Name</th>
                                <th>Phone</th>
                                <th>Email</th>
                                <th>Account Total</th>
                            </tr>
                            <!--XSLT-->
                            <xsl:for-each select="accounts/client">
                                <xsl:sort select="account_total" order="ascending" data-type="number"/>
                                <tr id="client-row">
                                    <td><xsl:value-of select="name"/></td>
                                    <td><xsl:value-of select="phone"/></td>
                                    <!--Emails-->
                                    <td>
                                        <a title="Fake link!">
                                            <xsl:attribute name="href">
                                                mailto:<xsl:value-of select="email"/>
                                            </xsl:attribute>
                                            <xsl:value-of select="email"/>
                                        </a>
                                    </td>
                                    <!--Account Totals-->
                                    <xsl:choose>
                                        <xsl:when test="account_total &lt;= '80000'">
                                            <td class="less">&#36;<xsl:value-of select="account_total"/></td>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <td class="total">&#36;<xsl:value-of select="account_total"/></td>
                                        </xsl:otherwise>
                                    </xsl:choose>       
                                </tr>
                            </xsl:for-each>
                        </table>
                    </main>
                    <!--FOOTER-->
                    <footer>
                        <!--Copyleft-->
                        <button id="license">
                            <a href="https://creativecommons.org/licenses/by-sa/4.0/" title="CC BY-SA 4.0" target="_blank" id="cc"></a>
                            <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="Creative Commons icon"/>
                            <img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="Creative Commons Attribution icon"/>
                            <img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="Creative Commons ShareAlike icon"/>
                        </button>
                        <p id="attribution">2026 <a href="mailto:jlenzi@mail.ccsf.edu?subject=Re:CNIT-131A" title="Email me">Jules Lenzi</a></p>
                    </footer>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
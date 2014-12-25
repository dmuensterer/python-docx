.. _understandingstyles:

Understanding Styles
====================

**Grasshopper:**
    *"Master, why doesn't my paragraph appear with the style I specified?"*

**Master:**
    *"You have come to the right page Grasshopper; read on ..."*


What is a style in Word?
------------------------

Documents communicate better when like elements are formatted consistently. To
achieve that consistency, professional document designers develop a *style
sheet* which defines the document element types and specifies how each should
be formatted. For example, perhaps body paragraphs are to be set in 9 pt Times
Roman with a line height of 11 pt, justified flush left, ragged right. When
these specifications are applied to each of the elements of the document,
a consistent and polished look is achieved.

A style in Word is such a set of specifications that may be applied, all at
once, to a document element. Word has paragraph styles, character styles, table
styles, and numbering definitions. These are applied to a paragraph, a span of
text, a table, and a list, respectively.

Experienced programmers will recognize styles as a level of indirection. The
great thing about those is it allows you to define something once, then apply
that definition many times. This saves the work of defining the same thing
over an over; but more importantly it allows you to change the definition and
have that change reflected in all the places you have applied it.


Why doesn't the style I applied show up?
----------------------------------------

This is likely to show up quite a bit until I can add some fancier features to
work around it, so here it is up top.

#. When you're working in Word, there are all these styles you can apply to
   things, pretty good looking ones that look all the better because you don't
   have to make them yourself. Most folks never look further than the built-in
   styles.

#. Although those styles show up in the UI, they're not actually in the
   document you're creating, at least not until you use it for the first time.
   That's kind of a good thing. They take up room and there's a lot of them.
   The file would get a little bloated if it contained all the style
   definitions you could use but haven't.

#. If you apply a style using |docx| that's not defined in your file (in the
   styles.xml part if you're curious), Word just ignores it. It doesn't
   complain, it just doesn't change how things are formatted. I'm sure
   there's a good reason for this. But it can present as a bit of a puzzle if
   you don't understand how Word works that way.

#. When you use a style, Word adds it to the file. Once there, it stays.
   I imagine there's a way to get rid of it, but you have to work at it. If
   you apply a style, delete the content you applied it to, and then save the
   document; the style definition stays in the saved file.

All this adds up to the following: If you want to use a style in a document you
create with |docx|, the document you start with must contain the style
definition. Otherwise it just won't work. It won't raise an exception, it just
won't work.

If you use the "default" template document, it contains the styles listed
below, most of the ones you're likely to want if you're not designing your own.
If you're using your own starting document, you need to use each of the styles
you want at least once in it. You don't have to keep the content, but you need
to apply the style to something at least once before saving the document.
Creating a one-word paragraph, applying five styles to it in succession and
then deleting the paragraph works fine. That's how I got the ones below into
the default template :).


Glossary
--------

style definition
    A ``<w:style>`` element in the styles part of a document that explicitly
    defines the attributes of a style.

defined style
    A style that is explicitly defined in a document. Contrast with *latent
    style*.

built-in style
    One of the set of 276 pre-set styles built into Word, such as "Heading
    1". A built-in style can be either defined or latent. A built-in style
    that is not yet defined is known as a *latent style*. Both defined and
    latent built-in styles may appear as options in Word's style panel and
    style gallery.

custom style
    Also known as a *user defined style*, any style defined in a Word
    document that is not a built-in style. Note that a custom style cannot be
    a latent style.

latent style
    A built-in style having no definition in a particular document is known
    as a *latent style* in that document. A latent style can appear as an
    option in the Word UI depending on the settings in the |LatentStyles|
    object for the document.

recommended style list
    A list of styles that appears in the styles toolbox or panel when
    "Recommended" is selected from the "List:" dropdown box.

Style Gallery
    The selection of example styles that appear in the ribbon of the Word UI
    and which may be applied by clicking on one of them.


Identifying a style
-------------------

A style has three identifying properties, `name`, `style_id`, and `type`.

Each style's :attr:`name` property is its stable, unique identifier for
access purposes.

A style's :attr:`style_id` is used internally to key a content object such as
a paragraph to its style. However this value is generated automatically by
Word and is not guaranteed to be stable across saves. In general, the style
id is formed simply by removing spaces from the *localized* style name,
however there are exceptions. Users of |docx| should generally avoid using
the style id unless they are confident with the internals involved.

A style's :attr:`type` is set at creation time and cannot be changed.


Style inheritance
-----------------

A style can inherit properties from another style, somewhat similarly to how
Cascading Style Sheets (CSS) works. Inheritance is specified using the
:attr:`~.BaseStyle.base_style` attribute. By basing one style on another, an
inheritance hierarchy of arbitrary depth can be formed. A style having no
base style inherits properties from the document defaults.


Paragraph styles in default template
------------------------------------

* Normal
* BodyText
* BodyText2
* BodyText3
* Caption
* Heading1
* Heading2
* Heading3
* Heading4
* Heading5
* Heading6
* Heading7
* Heading8
* Heading9
* IntenseQuote
* List
* List2
* List3
* ListBullet
* ListBullet2
* ListBullet3
* ListContinue
* ListContinue2
* ListContinue3
* ListNumber
* ListNumber2
* ListNumber3
* ListParagraph
* MacroText
* NoSpacing
* Quote
* Subtitle
* TOCHeading
* Title


Character styles in default template
------------------------------------

* BodyTextChar
* BodyText2Char
* BodyText3Char
* BookTitle
* DefaultParagraphFont
* Emphasis
* Heading1Char
* Heading2Char
* Heading3Char
* Heading4Char
* Heading5Char
* Heading6Char
* Heading7Char
* Heading8Char
* Heading9Char
* IntenseEmphasis
* IntenseQuoteChar
* IntenseReference
* MacroTextChar
* QuoteChar
* Strong
* SubtitleChar
* SubtleEmphasis
* SubtleReference
* TitleChar


Table styles in default template
--------------------------------

* TableNormal
* ColorfulGrid
* ColorfulGrid-Accent1
* ColorfulGrid-Accent2
* ColorfulGrid-Accent3
* ColorfulGrid-Accent4
* ColorfulGrid-Accent5
* ColorfulGrid-Accent6
* ColorfulList
* ColorfulList-Accent1
* ColorfulList-Accent2
* ColorfulList-Accent3
* ColorfulList-Accent4
* ColorfulList-Accent5
* ColorfulList-Accent6
* ColorfulShading
* ColorfulShading-Accent1
* ColorfulShading-Accent2
* ColorfulShading-Accent3
* ColorfulShading-Accent4
* ColorfulShading-Accent5
* ColorfulShading-Accent6
* DarkList
* DarkList-Accent1
* DarkList-Accent2
* DarkList-Accent3
* DarkList-Accent4
* DarkList-Accent5
* DarkList-Accent6
* LightGrid
* LightGrid-Accent1
* LightGrid-Accent2
* LightGrid-Accent3
* LightGrid-Accent4
* LightGrid-Accent5
* LightGrid-Accent6
* LightList
* LightList-Accent1
* LightList-Accent2
* LightList-Accent3
* LightList-Accent4
* LightList-Accent5
* LightList-Accent6
* LightShading
* LightShading-Accent1
* LightShading-Accent2
* LightShading-Accent3
* LightShading-Accent4
* LightShading-Accent5
* LightShading-Accent6
* MediumGrid1
* MediumGrid1-Accent1
* MediumGrid1-Accent2
* MediumGrid1-Accent3
* MediumGrid1-Accent4
* MediumGrid1-Accent5
* MediumGrid1-Accent6
* MediumGrid2
* MediumGrid2-Accent1
* MediumGrid2-Accent2
* MediumGrid2-Accent3
* MediumGrid2-Accent4
* MediumGrid2-Accent5
* MediumGrid2-Accent6
* MediumGrid3
* MediumGrid3-Accent1
* MediumGrid3-Accent2
* MediumGrid3-Accent3
* MediumGrid3-Accent4
* MediumGrid3-Accent5
* MediumGrid3-Accent6
* MediumList1
* MediumList1-Accent1
* MediumList1-Accent2
* MediumList1-Accent3
* MediumList1-Accent4
* MediumList1-Accent5
* MediumList1-Accent6
* MediumList2
* MediumList2-Accent1
* MediumList2-Accent2
* MediumList2-Accent3
* MediumList2-Accent4
* MediumList2-Accent5
* MediumList2-Accent6
* MediumShading1
* MediumShading1-Accent1
* MediumShading1-Accent2
* MediumShading1-Accent3
* MediumShading1-Accent4
* MediumShading1-Accent5
* MediumShading1-Accent6
* MediumShading2
* MediumShading2-Accent1
* MediumShading2-Accent2
* MediumShading2-Accent3
* MediumShading2-Accent4
* MediumShading2-Accent5
* MediumShading2-Accent6
* TableGrid
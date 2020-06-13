# oneschool

## Analyse partie cour du template de l'app service

## Cours

    image:ImageField
    prix:FloatField
    durée:DurationField
    nombre de chapitre=IntegerField
    cour:CharField
    description:TextField
    etudiants:IntegerField
    commentaire:: ===> Forenkey
    teahers: ===> Forenkey

### Teacher

    -nom:CharField
    -prenom: CharField
    -image:ImageField
    -cour dispancer:===> ManyToOneField
    -description: ===> TextField

### Etudiants

    -nom:CharField
    -cours suivis: ===> ManyToManyField

### Commentaire

    -nom:CharField
    -prenom:CharField
    -photo:ImageField
    -message:TextField
    -cours:===>Forenkey


### Programmes

    -image: ImageField
    -titre: CharField
    -description: TextField
    -nombre de diplomer : IntergerField
    -situation: UrlField
    -debut_cours : ===> DateTimeField
    -fin_cours :===> DateTimeField  